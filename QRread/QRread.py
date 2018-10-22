from pyzbar.pyzbar import decode
from PIL import Image

def main():
	image = 'test.png' #QRコードの画像
	data = decode(Image.open(image))	#QRコードのデータ全体
	QRtext = str(data).split('\'')[1]	#QRコードのテキスト部分
	print(QRtext);
	QRText_s =  QRtext.replace(' ',',')
	_yLen = int(QRtext.split(':')[0].split(' ')[0])	#ステージの縦*横(_yLen*_xLen)
	_xLen = int(QRtext.split(':')[0].split(' ')[1])
	Agentx = int(QRtext.split(':')[_yLen+1].split(' ')[0])-1	#1Pの1人目のエージェントのx,y座標
	Agenty = int(QRtext.split(':')[_yLen+1].split(' ')[1])-1
	#self._1PAgents = [Agent([Agenty, Agentx],1),Agent([_yLen - 1 - Agenty, _xLen - 1 - Agentx],1)] #ステージに存在する1Pのエージェントのリスト
	#self._2PAgents = [Agent([_yLen - 1 - Agenty, Agentx],2),Agent([Agenty, _xLen - 1 - Agentx],2)] #ステージに存在する2Pのエージェントのリスト		
	#self._Panels = [[Panel(0) for i in range(_xLen)]for j in range(_yLen)] #パネルの配列の作成

	#パネルのスコア設定
	"""
	for y in range(_yLen):
		PanelsScores = QRtext.split(':')[y+1]
		for x in range(_xLen):
			PanelScore = int(PanelsScores.split(' ')[x])
			self._Panels[y][x] = Panel(PanelScore)
	"""

	#バイナリ書き込み
	data = list(QRtext);
	with open('StageInfo.bin','wb') as f:
		for d in data:
			f.write(ord(d).to_bytes(1,'little'))

if __name__ == '__main__':
	main()