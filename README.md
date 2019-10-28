# **wordipy**
wordipy is dummy  package which can be used to get abbrevations, tupled things, amounts written in letter to numbers. 

## Dependencies

The following needs to be installed if you dont have it.
- Python 3 (3.7 or higher)
-  NLTK
    <br /> `pip install --user -U nltk`
	 <br />  or <br /> `conda install -c anaconda nltk`
- word2number
 <br />`pip install word2number`  <br /> or <br />
`conda install -c conda-forge word2number`
--------------------------------

>Clone this repository
```
git clone https://github.com/amitjslearn/wordipy.git
```
>Open the terminal, cd into the directory where the file is cloned

Open python in terminal (or command prompt)
. Type `python` if you have anaconda or `python3`
``` python
Python 3.7.3 (default, Mar 27 2019, 22:11:17) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
## Usage
``` python
>>> from wordipy.main import abbreviationize
>>> abbreviationize("C M")
'CM'
>>> abbreviationize("Triple A")
'AAA'
>>> abbreviationize('Double Bam', sep=",")
'Bam, Bam'
```
>for more help type `help(abbreviationize)`
``` python
>>> help(abbreviationize)
```
----
``` python
>>> from wordipy.main import amountize
>>> amountize("three hundred dollars")
'$300'
>>> amountize("two yen")
'¥2'
```
>for more help type `help(amountize)`
``` python
>>> help(amountize)
```
---
### Further improvements/additional features:
1) abbreviationize: input to abbreviationize should be a capital like "C M" to get the output as CM 
for ex c m will not give CM

2) amountize: the amount which is already a number can be retained as it is
3) Stop words can be removed if needed
4) **Lemmatization** and **stemming** can be done properly wherever required

>**Note**    
>1) Only most commonly used tuples (like single, double, triple, quadruple) are used, other tuples can be added as per the needs.
>2) Only some of the currencies are added (like dollar, yen) other currencies can be added if required.