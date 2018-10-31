import os

class sjPath():
    
    def getAllPath(dirpath, *suffix):
        """
        :suffix[] 文件格式
        """
        PathArray = []
        for r, ds, fs in os.walk(dirpath):
            for fn in fs:
                if os.path.splitext(fn)[1] in suffix:
                    fname = os.path.join(r, fn)
                    PathArray.append(fname)
        return PathArray
   
    def departWrite(self, root,path,departSymbol="/"):
        print(os.getcwd())
        l= path[ :3]+departSymbol+path[3:6]
        if os.path.exists(root+l)==False:
            os.makedirs(root+l)
        return root+l+"/"+path


from string import digits
    
class sjtext():
    def delDigits(s):
        remove_digits = s.maketrans('', '', digits)
        return s.translate(remove_digits)