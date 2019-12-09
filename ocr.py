from cnocr import CnOcr
import resp
import const

ocr = CnOcr()
def discern(filePath):
	respVo = resp.RespVo()
	if filePath.strip() == '':
		respVo.code = const.FILE_PATH_IS_NULL
		respVo.message = 'FILE_PATH_IS_NULL'
	else:
		respVo.code = const.OK
		respVo.message = 'OK'
		respVo.data = ocr.ocr(filePath)
	return respVo