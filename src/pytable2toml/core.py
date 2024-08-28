r"""Core functions"""
import argparse
import tomlkit


def get_toml(fpath: str, skipheader:int=0, delimiter:str=" ")->tomlkit.document:
    
    toml = tomlkit.document()
    
    k = 1
    header_flag = False
    fpath = fpath
    with open(fpath, "r") as f:
        for line in f:
            line = line.replace("\n", "")
            if not header_flag:
                if k == (skipheader+1):
                    header = line.split()
                    header_flag = True
            else:    
                values = line.split()
        
                di = dict(zip(header[1:], values[1:]))
                toml.update({values[0]: di})

            k += 1

    fpath = fpath.replace(".txt",".toml")
    with open(fpath, "w") as f:
        f.write(tomlkit.dumps(toml))

    return toml

if __name__ == "__main__":
    pass
