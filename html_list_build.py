#monsijb
#define the  html_list function
def html_list(input_strings):
    output_strings = [];
    output_strings.append("<ul>")
    for iter_string in input_strings:
        new_str = "<li>{}</li>".format(iter_string)
        output_strings.append(new_str)
    output_strings.append("</ul>")
    return("\n".join(output_strings))
    

test_list = ['first string', 'second string']
print(html_list(test_list))
