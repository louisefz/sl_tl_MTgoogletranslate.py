import os
import sys
import xml.etree.ElementTree as ET
import glob



# os.chdir("/Users/zhoujie/Desktop/未命名文件夹 2")  # indir为xml文件来源的文件夹，outdir为转换的txt文件存储路径
# annotated = os.listdir('.')  # 返回包含目录中文件名称的列表
# print(annotated)
def xml2txt(path):
    new_path = path.replace(".xml",".txt")
    with open(path) as f:
        xml_content = f.read()
        xml_processed = ET.fromstring(xml_content)
        text_content_byte = ET.tostring(xml_processed, method='text')
        print(type(text_content_byte))
        text_content_str = str(text_content_byte, encoding="utf-8")
        with open(new_path,"w") as t:
            t.write(text_content_str)
xml2txt("/Users/zhoujie/Desktop/paper_project/CLEAN_XML/A/A0/A08.xml")




