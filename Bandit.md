# THIS IS WHERE I WILL STORE ANYTHING LEARNT FROM OTW.ORG


## LEVEL 1

**ls** - lists storage
*ls -a*- lists everything in the current directory, including hidden files

**cd {dir_path}** - changes into specified directory
*cd..*- move back a level in the terminal

**cat {filename}** - print the information within a file

**file {filename}** - prints the file type, could be between[text, executable and data for anything else]

**du {filename}** - estimates file space usage
*du -h {filename}*- the info is printed in human readable format

**find <where> <what>** - Searches the current directory for the file or directory. if directory, it proceeds to print all contents including the hidden files


## LEVEL 2

There are special filenames that are treated different by UNIX systems.
Such filenames include, **-**, **--** and *.
To perorm normal commands on thee files you'll need to either

**Prefix them with *./*.**

**Use their full (relative) path like *~/-* or */home/spectre/{path_to_file}*.**

**Use redirection eg. *{command} < -*.**

Otherwise your command will wait for input from U.

## LEVEL 3

## LEVEL 4

## LEVEL 5

## LEVEL 6

**find <where> <what>**- can take arguments that makes it very versatile tool e.g
**-type** - where it takes the params "f" for files and "d" for dirs

**-name** - takes the name as params, use *.<filetype> for wildcards.

**-iname** - case-insensitive type of *-name*

**-size** - +10M(10MB or larger), -1K(smaller than 1kb) G, M, K

**-maxdepth** - search how deep in terms of levels i.e 1 for in this dir only

**-exec** - is the execute argument takes "{}" as the placeholder for the files found, and when done with the command U want executed for the file postpend it with "\;" e.g
    find . -name "*.log" -exec rm {} \; # deletes all .log files in the current dir

## LEVEL 7

**find /** - Start searching from root directory

**-type f** - Only look for FILES (not directories/symlinks)

**-group bandit6** - File must belong to GROUP 'bandit6'

**-perm /g=r** - File must be READABLE by the group

**-size 33c** - File must be exactly 33 BYTES (c = characters/bytes)

**2>/dev/null** - Hide ALL error messages (permission denied, etc.)

**-exec cat {} \;** - For each matching file, RUN 'cat' on it

## LEVEL 8

**strings** - is a utility used to extract and print human-readable character sequences from binary files 
    Format: strings [options] <binary_file>
    -n <length>: Minimum string length (default 4)
    -t {d,o,x}: Show offset in decimal/octal/hex
    -e {s,l,b}: Character encoding (7-bit, 16-bit big/little endian)

    strings /bin/ls | head -20           # See embedded text in ANY binary
    strings memory.dump | grep pass      # Hunt credentials in memory
    strings -n 10 file.exe               # Only strings ≥10 chars
    strings -tx malware.bin              # Hex offsets for forensics
    cat encrypted.raw | strings          # Find plaintext in encrypted data

No args needed: Just pipe any binary through it

**|** - parses the output from the left command  as input to the right command. e.g
*cat data.txt | grep "millionth"*
    - the command above parses the content of "data.txt" as input to *grep* which then gets the line containing the word "millionth"

**sort data.txt | uniq -u** - 
    *uniq -u*- only checks for and prints unique objects if they are adjacent, and so it's versatility is enhanced by the command *sort*