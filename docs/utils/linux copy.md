# linux

!!! p  tricks
    - `clear` 清空当前界面

## 查看

- `pwd` 现在在哪

- `ls` 当下目录里有什么
`ls /tmp`
`ls -al`
- `cat <file_name>` 查看文件内容
`cat output.txt`
    > `cat test_1.txt test_2.txt test_3.txt` 连续查看三个txt的内容，one after the other, as a single block of text
    > `cat t*` 查看所有以t开头的文件

## 移动 - 到达地址

!!! p “/” directory is sometimes referred to as the root directory

- cd
`cd ..` 上一层
`cd` 单纯的cd是回到home directory
`cd ../ ..` 回到上层的上层
`cd /home/`
- `mv <file_name> <directory>` 将文件移动到directory. <u>记得`ls` confirm</u>
    > `mv file_1.txt dir1`
- `cp <file1_name> <copy_name>` 复制副本

## 创建 -删除

- `mkdir <file_name_1>, <file_name_2>, …` 在当前目录下创建多个目录
注意如果是写的是比较长的路径，就会都创建出来
    > `mkdir /tmp/tutorial` 创建了tmp，再在tmp下创建tutorial
    `mkdir dir1 dir2 dir3` 连创三个directory
- `cat > <new_file.txt>` 创建新的文档

---

- `rm <file1_name> <file2_name>` 连续删除多个文档
    > `rm *.txt` 删除全部txt文档
    > `rm test1.txt`
- `rm -r <directory_name>` 删除整个文件夹without confirmation

!!! danger 删除的文件是不会放进垃圾箱的，也就是说删除之后不能找到

### 编辑保存

关键是 `> <output_file_name>`  

增加 appending file： `>> <output_file_name>`

`ls > output.txt` 在当前目录下创建一个output的txt 储存file list的内容

- cat: (short for concatenate) command is one of the most frequently used commands on Linux
`cat t* > combine.txt` 将当前目录下所有以t开头的文件合并生成combine.txt

- `echo “I ve append a new line” >> combine.txt` 在combine.txt里新增一串文字

- `mv <file_name> <file_new_name>` 重命名

### 软件

`apt-get update` 更新Update the software sources
`apt-get install <software_name>` 下载
>`apt-get install vim` 下载vim 编辑器
