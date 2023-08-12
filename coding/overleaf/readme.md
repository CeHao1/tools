
# Structure
1. include packages and define commands before the main content
2. use \input{} to insert the sections
3. add reference \bibliography{references} 


# Equation

## include
```
\usepackage{amsmath}
\usepackage{amssymb}
```

## tools
[mathpix](https://mathpix.com/) offline compile and OCR.  
[texmath](https://github.com/jgm/texmath) convert word equation to latex, or vice versa.

## format 
* in-text equation: ``` $equation$ ```  
* separate equation: ``` \begin{equation} \end{equation}```
* align: ```\begin{align}``` and use ```&``` to align equations
* no-number: ```\nonumber```
* underset: ```\underset{a}{b}```, b is on top of a

## font 
* empty space: ```~```
* Bold ```\textbf{}```
* Emphasize  ```\textit{} , \emph{}```
* underline ```\underline```
* calligraphy ```\mathcal{}```
* blackboard bold ```\mathbb{}``` 
* operation name ```\operatorname{argmax}```
* bracket: [detail](https://blog.csdn.net/m0_37864814/article/details/102854015) ```\[ \], \left[ \right] \big[ \big]```
* not finished bracket: ```\left. \right.```

---
---
# Figure
## include
```
\usepackage{graphicx}
\usepackage{wrapfig} # wrap the figure with text
\usepackage{subfigure} # use multiple figures
```

## add figures
```
\begin{figure}[t]
    \centering
    \includegraphics[width = 0.8\textwidth]{figure_name.png}
    \caption{Caption}
    \label{Fig: xx}
\end{figure}
```
* one-column figure in two-column article ```\begin{figure*}```
* figure wrapped with text ```\begin{warapfigure}```
* subfigure [detal](https://blog.csdn.net/u010440456/article/details/113760134) ```\subfigure[name]{\includegraphics{figure_name}}```

# Table

## include
```
\usepackage{threeparttable} # add table footnote
\usepackage{makecell} # seperate one cell
```

## add table
[detail](https://blog.csdn.net/weixin_50637207/article/details/126166763)  
[generator](https://www.tablesgenerator.com/)  
threeparttable is not necessary, if not using tablenotes

```
\renewcommand\arraystretch{1.5}  # set hight of lines
\begin{table}[t]
    \centering
    \caption{xx}

    \begin{threeparttable}
        \begin{tabular}{l|c c} # main content
        # left, center, right, 
        # p{2pt} to control width
        \multicolumn{2}{|c|}{xxx} # combine to columns as one cell & xxx \\ # new row  
        \hline # a horizontal line
        \multirow{2}*{xx} & xx & xx \\
        \cline{2-3} # hline, but shorter
        \end{tabular}

        \begin{tablenotes} # add table notes
            \item[1]
            \item[*]
        \end{tablenotes}

    \end{threeparttable}
\end{table}
```


# Algorithm
## include
```
\usepackage{algorithm}
\usepackage[noend]{algorithmic} # a separate file
```

## add algorithm
```
\begin{algorithm}[t]
\caption{xx} # title of this algorithm
\begin{algorithmic}[1] # numbered with 1,2,3
\STATE \textbf{Input: }
\FOR{} # will have indent
    \IF{} # indent
        \STATE xx \COMMENT{} # add comment at last
    \ELSE
        \STATE
    \ENDIF
\ENDFOR
\STATE \textbf{Return: } xx
\end{algorithmic}
\end{algorithm}
```

Can add smaller algorithm via 
```
\begin{wrapfigure}{r}{0.6\textwidth} # right smaller figure
\begin{minipage}{0.6\textwidth} # smaller equation
```


# Reference
* add label: ```\label{}```, name space: Eqn, Fig, Table, Alg, Sec, Subsec, Appendix
* cite: ```xx~\ref{}``` or ```\eqref{}```(has eqn bracket)
* ref: ```\ref{}``` 
* url: [detail](https://www.overleaf.com/learn/latex/Hyperlinks)
```
\usepackage{hyperref}       % hyperlinks
\usepackage{url}            % simple URL typesetting

\href{website link}{web name}
\url{http://www.overleaf.com} # cannot edit its name
```

# Color
## include
```
\usepackage{color}
\usepackage{xcolor}
```
[detail](https://www.overleaf.com/learn/latex/Using_colours_in_LaTeX)

## add color to text
* add to only a few words ```\textcolor{red}{content}``` or ```{\color{red} content}```
* add to the following ```\color{red}```
* change intensity: ```\color{red!80}``` only 80%
* define color:
```
\definecolor{mypink1}{rgb}{0.858, 0.188, 0.478}
\definecolor{mypink2}{RGB}{219, 48, 122}
\definecolor{mypink3}{cmyk}{0, 0.7808, 0.4429, 0.1412}
\definecolor{mygray}{gray}{0.6}
```
* color background: ```\colorbox{red}{content}```

# New command

## example: 
```
\newcommand{\commandname}[number_of_arguments]{definition}
\newcommand{\greeting}[1]{Hello, #1!} # 1 argument
\newcommand{\fullname}[2]{Full Name: #1 #2} # two arguments

\greeting{John}
\fullname{John}{Smith}
```

## advanced usage
```
\newcommand{\red}[1]{{\textcolor{red}{#1}}}
\red{content}
```