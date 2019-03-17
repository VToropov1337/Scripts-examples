import argparse



def get_args():
    parser = argparse.ArgumentParser(description='Videos to images')
    parser.add_argument('indir', type=str, help='Input dir for videos')
    parser.add_argument('outdir', type=str, help='Output dir for image')
    args = parser.parse_args()
    return args.indir, args.outdir
# print(args.indir,args.outdir)







def check_params(indir,outdir):
    if isinstance(indir,str) and outdir.isalpha():
        print('gg')
    else:
        raise TypeError('Wrong arguments')
        
        
        
        
        
if __name__ == '__main__':
    p1, p2 = get_args()
    check_params(p1,p2)
