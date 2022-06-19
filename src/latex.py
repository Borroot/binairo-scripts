TEMPLATE_START = \
"""\\documentclass[a4paper]{article}

\\usepackage[margin=2cm]{geometry}
\\usepackage{anyfontsize}
\\usepackage{graphicx}
\\usepackage{subcaption}

\\begin{document}
\\pagenumbering{gobble}

\\hspace{0pt}
\\vspace{6cm}
\\begin{center}
	\\fontsize{80}{100}\\selectfont \\textbf{Binairo} \\normalsize\\\\
	\\vspace{1cm}
	\\LARGE \\normalsize
\\end{center}
\\vfill
\\hspace{0pt}

"""


TEMPLATE_END = \
"""\\end{document}
"""

# TODO {number:02d} assumes maximum of 99p.png
def latex_puzzle(foldername, amount):
    builder = ""
    for number in range(amount):
        builder += (
            "\\pagebreak\n"
            "\\hspace{0pt}\n"
            f"\\flushright \\fontsize{{50}}{{60}}\\selectfont \\textbf{{{number + 1}}} \\normalsize\n"
            "\\vfill\n"
            "\\begin{figure}[h]\n"
            "    \\centering\n"
            f"    \\includegraphics[width = 0.8\\textwidth]{{{foldername}/{number:02d}p.png}}\n"
            "\\end{figure}\n"
            "\\vfill\n"
            "\\hspace{0pt}\n\n"
        )
    return builder


# TODO {number:02d} assumes maximum of 99p.png
def latex_solutions(foldername, amount):
    builder = ""

    for number in range(0, amount, 3):
        builder += "\\begin{figure}\n\\centering\n"
        for i in range(3):
            if number + i < amount:
                builder += (
                    "\\begin{subfigure}{0.3\\textwidth}\n"
                    f"    \\includegraphics[width=\\textwidth]{{{foldername}/{number + i:02d}s.png}}\n"
                    f"    \\center {number + i + 1}\n"
                    "\\end{subfigure}\n"
                    "\\hfill\n"
                )
        builder += "\\end{figure}\n\n"

    return builder


def booklet(foldername, amount):
    if amount > 99:
        raise NotImplemented

    builder  = TEMPLATE_START
    builder += latex_puzzle(foldername, amount)
    builder += latex_solutions(foldername, amount)
    builder += TEMPLATE_END

    return builder
