# Store html operating and hiragana processing functions
# 包含了文件操作、html转换、假名注音等基本函数
import os
import sys
import traceback
import copy
import zipfile

from bs4 import BeautifulSoup
import pykakasi
kks = pykakasi.kakasi()  # 创建假名注音器
def is_kanji(char):
    return '\u4e00' <= char <= '\u9fff'

def has_kanji(string):
    return any(map(is_kanji, string))


def p2kana(p,soup):
    """
    在html中<p>标签内添加<ruby>以添加假名。
    新建<p>标签，扫描原标签中所有元素，若为可注音的字符串进行注音，否则原样复制。
    p: bs4中获取的p标签
    soup： 网页对象
    """

    p_new = copy.copy(p)
    p_new.contents = []
    p_copy = copy.copy(p)
    for child in p_copy.contents:
        if isinstance(child,str):
            kana2str(child,p_new,soup)
        elif has_strings(child):
            if child.name == 'ruby':
                p_new.append(copy.copy(child))
            else:
                child_copy = copy.copy(child)
                child_copy.contents = []

                for subchild in child.contents:
                    if isinstance(subchild,str):
                        kana2str(subchild, child_copy, soup)
                    else:
                        child_copy.append(copy.copy(subchild))
                child = child_copy
                p_new.append(child)
        else:
            p_new.append(child)

    p.replace_with(p_new)


def has_strings(tag):
    # 判断标签中是否含有字符串
    return not len(list(tag.strings)) == 0

def kana2str(string,tag_copy,soup):
    """
    含汉字字符串处理，生成对应的html注音格式
    :param string: 待处理字符串
    :param tag_copy: 待处理标签，一般为<p>和<span>
    :param soup: 待处理网页
    """
    for word in kks.convert(string):
        if has_kanji(word['orig']):
            new_ruby_tag = soup.new_tag('ruby')
            new_rb_tag, new_rt_tag = soup.new_tag('rb'), soup.new_tag('rt')
            new_rb_tag.string, new_rt_tag.string = word['orig'], word['hira']

            new_ruby_tag.append(new_rb_tag)
            new_ruby_tag.append(new_rt_tag)
            tag_copy.append(new_ruby_tag)
        else:
            tag_copy.append(word['orig'])


def para_loop(page):
    for para in page.find_all('p'):
        p2kana(para,page)

def append_hirakana_to_webpage(file:str):
    # 将网页替换为注音后的网页
    if is_web_page(file):
        with open(file,'r',encoding='utf-8') as webfile:
            webpage = BeautifulSoup(webfile,'html.parser')
        para_loop(webpage)  # 对网页中的所有段落进行处理
        with open(file,'w',encoding='utf-8') as file:
            file.write(str(webpage))


def deldir(dir):
    # 删除文件夹及所有文件
    for item in os.listdir(dir):
        tmp = os.path.join(dir,item)
        if os.path.isdir(tmp):
            deldir(tmp)
        else:
            os.remove(tmp)
    os.rmdir(dir)

def is_web_page(file:str):
    return file.endswith('.html') or file.endswith('.xhtml')

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),os.path.relpath(os.path.join(root, file), path))

def zip_epub(path,out_path):
    with zipfile.ZipFile(out_path,"w",zipfile.ZIP_DEFLATED) as zipf:
        zipdir(path,zipf)

def resource_path(relative_path):
    # pyinstaller识别路径
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)