import os
from markdown_blocks import markdown_to_html_node
from gencontent  import extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Generating Page for {dir_path_content} to {dest_dir_path}")
    if os.path.isdir(dir_path_content):

        print(f"{dir_path_content} is a directory")
        for paths in os.listdir(dir_path_content):
            src = os.path.join(dir_path_content, paths)

            dst_dir = os.path.join(dest_dir_path, paths)
            if os.path.isdir(src):
                os.makedirs(dst_dir, exist_ok=True)
                generate_pages_recursive(src, template_path, dst_dir)
                    
            elif os.path.isfile(src):

                stem = os.path.splitext(paths)[0]
                dst_file = os.path.join(dest_dir_path, stem + ".html")
                name, ext = os.path.splitext(paths)
                if ext.lower() != ".md":
                    return
                print(f" * {src} {template_path} -> {dst_file}")
                

                from_file = open(src, "r")
                markdown_content = from_file.read()
                from_file.close()

                template_file = open(template_path, "r")
                template = template_file.read()
                template_file.close()

                node = markdown_to_html_node(markdown_content)
                html = node.to_html()

                title = extract_title(markdown_content)
                template = template.replace("{{ Title }}", title)
                template = template.replace("{{ Content }}", html)


                to_file = open(dst_file, "w")
                to_file.write(template)



