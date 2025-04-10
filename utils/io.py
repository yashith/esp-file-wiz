from os import path


def get_in_out_files(args:list[str]) -> tuple[str,str] | None:
    files = None
    if len(args) ==3:
        files = (args[1],args[2])
    elif len(args) == 2:
        # TODO additional validations required eg: file type a valid path 
        out_file = path.basename(args[1]).replace("xml","graphml")
        files = (args[1],out_file)
    return files
