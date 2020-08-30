import os

folders='C:/Users/chenl/Pictures/Screenshots/'

def png_md_transform(from_folders, to_files):
    with open(to_files,'w+',encoding='utf-8') as f:
        for item in os.listdir(folders):
            if item.endswith('png') or item.endswith('jpeg'):
                f.writelines("<img src={} style='zoom:200%' />".format(folders+item))
                #f.writelines('![{}]({}=100*100) \n'.format(item,folders+item))
                f.writelines('\n')

if __name__ == '__main__':
    png_md_transform(folders,'C:/Users/chenl/Desktop/files.md')


