#Encrypt Talha Technology
#Github : https://github.com/TermuxTalha
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))