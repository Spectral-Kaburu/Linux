# Welcome to the beautiful life of the CLI!!!

## grep

used to search for strings in files or output
prints the line with the string

**grep {string} {file}** 


### flags/params/args

**-c** counts the number of times that the string occured

**-i** string being seached becomes case insensitive

**-v** prints the lines that are not matched

**-x** matches the whole line, so a line is given

**-w** matches the whole string, not the chracters

**-e or --** helps search flags in man pages

**-B {n}** n is the number of lines before the string, they will be printed

**-A {n}** lines after said string will be printed too

**-E** to use extended regex that allows for special characters


### string manipulation

**"^{string}"** prints the line that has the string in the beinning of it

**"{string}$"** prints the line with the string at the end

**\b{string}** prints the line with the string at the start
    try this on a html file **grep '^<.*>$'**

grep uses basic regular expression(regex) {look extended regular expression too} which only allows special characters if they are escaped
    eg. **grep '404\|500' *.logs** the pipe character is a special character and so requires to be escaped


### integer manipulation

**'4[0-9][0-9]'** check for numbers between 400 & 499

**-E '([0-9]{3}\.){3}[0-9]{1,3}'** looks through ip address, checks that the first octet has 3 digits and the last octet has 1,2,3 digits 
    e.g *203.302.781.123*, *304.489.283.3*, *323.902.448.74*

