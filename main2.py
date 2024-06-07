import glob
import Query
import ReadAllTypeFiles
import ranked_retreval
def Result(query):
    files = glob.glob("testfile/*")
    files = list(files)
    result_text = ranked_retreval.Rank(ReadAllTypeFiles.ReadFile(files), Query.query(query))
    return result_text