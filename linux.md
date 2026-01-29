# Welcome to the beautiful life of the CLI!!!

## grep

used to search for strings in files or output
prints the line with the string

**grep {string} {file}** 


### flags

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

## nmap

It's a network mapper.

***nmap [flags] [target]***

**nmap [target]**, looks at 1000 famous ports and shows their state and guesses the service

### states

**open** - an app is actively listening
**closed** - accessible, receives an responds to nmap packets but have no apps listening
**un/filtered** -  nmap can't determine whether it's open or close, usually due to firewalls or router
**open/closed|filtered** - can't tell if it's open/closed or filtered

### targets

Ip addresses normaly
U can use **/** to specify a range. e.g **10.0.1.0/24**

### flags

**-O** - used to check the OS
**-A** - kinda wraps up the *-O*, Aggressive
**-s** - scan type followed by uppercase *signifier*
    #### signifiers
    **L** - list
    **n** - pings the ip address
    **V** - looks at the version of the app running
    **S** - stealth scan

**-o** - output using signifiers
    **N** - normal output
    **X** - xml output
    **S** - script kitty output

**-p{port_num}** - scans specified ports
    if **-** passed as arg, it searches *all* ports

While nmap is running, check the command **"?"**

## regex {Regular Expressions} 
https://regexr.com/
A sequence of symbols and characters expressing a string or pattern to be searched for within a longer piece of text.

always defined with opening and closing **/**

### flags
**g** - global
**i** - case insensitive
/*I really need to come continue with this*/


## dirb
DIRB  IS  a Web Content Scanner. It looks for existing (and/or hidden) Web Objects. It basically works by launching a dictionary basesd attack against a web server and analizing the response.

**It is quite interesting look it up**
