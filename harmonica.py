from matplotlib.image import imread
from matplotlib import pyplot as plt,cm
import plotc

chromatic=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

key='A'
blow_bottom=True

keyind=chromatic.index(key)
scale=[]
scale.append(chromatic[keyind%12])
scale.append(chromatic[(keyind+2)%12])
scale.append(chromatic[(keyind+4)%12])
scale.append(chromatic[(keyind+5)%12])
scale.append(chromatic[(keyind+7)%12])
scale.append(chromatic[(keyind+9)%12])
scale.append(chromatic[(keyind+11)%12])

print "Key of",key
print

print "First position"
print "Root: 4 blow"
print key,"major:",scale
print key,"major pentatonic:",[scale[1-1],scale[2-1],scale[3-1],scale[5-1],scale[6-1]]
print key,"major blues:",[scale[1-1],scale[2-1],chromatic[(keyind+3)%12],scale[3-1],scale[5-1],scale[6-1]],"root 7 blow + 8 blow bend"

print
print "Second position"
print "Root: 2 draw or 6 blow"
print scale[4],"minor:",[chromatic[(keyind+7)%12],chromatic[(keyind+9)%12],
chromatic[(keyind+10)%12],chromatic[keyind],chromatic[(keyind+2)%12],chromatic[(keyind+3)%12],
chromatic[(keyind+5)%12]],"root 6 blow + 8 blow bend"
print scale[4],"minor pentatonic:",[chromatic[(keyind+7)%12],
chromatic[(keyind+10)%12],chromatic[keyind],chromatic[(keyind+2)%12],
chromatic[(keyind+5)%12]]
print scale[4],"minor blues:",[chromatic[(keyind+7)%12],
chromatic[(keyind+10)%12],chromatic[keyind],chromatic[(keyind+1)%12],chromatic[(keyind+2)%12],
chromatic[(keyind+5)%12]]
print scale[4],"major:",[chromatic[(keyind+7)%12],
chromatic[(keyind+9)%12],chromatic[(keyind+11)%12],chromatic[keyind],
chromatic[(keyind+2)%12],chromatic[(keyind+4)%12],chromatic[(keyind+6)%12]],"root 6 blow + 9 blow bend"
print scale[4],"major pentatonic:",[chromatic[(keyind+7)%12],
chromatic[(keyind+9)%12],chromatic[(keyind+11)%12],
chromatic[(keyind+2)%12],chromatic[(keyind+4)%12]]
print scale[4],"major blues:",[chromatic[(keyind+7)%12],chromatic[(keyind+9)%12],
chromatic[(keyind+10)%12],chromatic[(keyind+11)%12],chromatic[(keyind+2)%12],
chromatic[(keyind+4)%12]]
print scale[4],"major with dominant 7 (Mixolydian):",[chromatic[(keyind+7)%12],chromatic[(keyind+9)%12],
chromatic[(keyind+11)%12],chromatic[(keyind)%12],chromatic[(keyind+2)%12],
chromatic[(keyind+4)%12],chromatic[(keyind+5)%12]]

print
print "Third Position"
print "Root: 1 draw, 4 draw or 8 draw"
print scale[1],"Dorian:",[scale[1],scale[2],scale[3],scale[4],scale[5],scale[6],scale[0]]
print scale[1],"melodic minor:",[scale[1],scale[2],scale[3],scale[4],scale[5],scale[6],
chromatic[(keyind+1)%12]]
print scale[1],"minor:",[chromatic[(keyind+2)%12],chromatic[(keyind+4)%12],
chromatic[(keyind+5)%12],chromatic[(keyind+7)%12],chromatic[(keyind+9)%12],chromatic[(keyind+10)%12],
chromatic[keyind]]
print scale[1],"minor pentatonic:",[chromatic[(keyind+2)%12],
chromatic[(keyind+5)%12],chromatic[(keyind+7)%12],chromatic[(keyind+9)%12],
chromatic[keyind]]
print scale[1],"minor blues:",[chromatic[(keyind+2)%12],
chromatic[(keyind+5)%12],chromatic[(keyind+7)%12],chromatic[(keyind+8)%12],chromatic[(keyind+9)%12],
chromatic[keyind]]
print scale[1],"major:",[chromatic[(keyind+2)%12],chromatic[(keyind+4)%12],
chromatic[(keyind+6)%12],chromatic[(keyind+7)%12],chromatic[(keyind+9)%12],chromatic[(keyind+11)%12],
chromatic[(keyind+1)%12]]
print scale[1],"major with dominant 7:",[chromatic[(keyind+2)%12],chromatic[(keyind+4)%12],
chromatic[(keyind+6)%12],chromatic[(keyind+7)%12],chromatic[(keyind+9)%12],chromatic[(keyind+11)%12],
chromatic[keyind]]
print scale[1],"major pentatonic:",[chromatic[(keyind+2)%12],chromatic[(keyind+4)%12],
chromatic[(keyind+6)%12],chromatic[(keyind+9)%12],chromatic[(keyind+11)%12]]
print scale[1],"major blues:",[chromatic[(keyind+2)%12],chromatic[(keyind+4)%12],chromatic[(keyind+5)%12],
chromatic[(keyind+6)%12],chromatic[(keyind+9)%12],chromatic[(keyind+11)%12]]

print
print "Fourth Position"
print "This is the relative minor of first position"
print "Root: 3 bent a whole tone, or 6 draw"
print scale[5],"minor:",[scale[5],scale[6],scale[0],scale[1],scale[2],scale[3],scale[4]]
print scale[5],"minor pentatonic:",[scale[5],scale[0],scale[1],scale[2],scale[4]]
print scale[5],"minor blues:",[scale[5],scale[0],scale[1],chromatic[(keyind+3)%12],scale[2],scale[4]]
#~ print scale[5],"major:",[scale[5],scale[6],chromatic[(keyind+1)%12],chromatic[(keyind+2)%12],
#~ chromatic[(keyind+4)%12],chromatic[(keyind+6)%12],chromatic[(keyind+8)%12]],"not possible"
#~ print scale[5],"major pentatonic:",[scale[5],scale[6],chromatic[(keyind+1)%12],
#~ chromatic[(keyind+4)%12],chromatic[(keyind+6)%12],chromatic[(keyind+8)%12]],"not possible"

print
print "Fifth Position"
print "Root: 2 blow, 5 blow or 8 blow"
print scale[2],"Phrygian:",[scale[2],scale[3],scale[4],scale[5],scale[6],scale[0],scale[1]]
print scale[2],"minor:",[scale[2],chromatic[(keyind+6)%12],chromatic[(keyind+7)%12],
chromatic[(keyind+9)%12],chromatic[(keyind+11)%12],chromatic[keyind%12],chromatic[(keyind+2)%12]]
print scale[2],"minor pentatonic:",[scale[2],chromatic[(keyind+7)%12],
chromatic[(keyind+9)%12],chromatic[(keyind+11)%12],chromatic[(keyind+2)%12]]
print scale[2],"minor blues:",[scale[2],chromatic[(keyind+7)%12],
chromatic[(keyind+9)%12],chromatic[(keyind+10)%12],chromatic[(keyind+11)%12],chromatic[(keyind+2)%12]]
print scale[2],"major with dominant 7:",[scale[2],chromatic[(keyind+6)%12],chromatic[(keyind+8)%12],
chromatic[(keyind+9)%12],chromatic[(keyind+11)%12],chromatic[(keyind+1)%12],chromatic[(keyind+2)%12]]
print scale[2],"major pentatonic:",[scale[2],chromatic[(keyind+6)%12],
chromatic[(keyind+8)%12],chromatic[(keyind+11)%12],chromatic[(keyind+1)%12]]
print scale[2],"major blues:",[scale[2],chromatic[(keyind+6)%12],chromatic[(keyind+7)%12],
chromatic[(keyind+8)%12],chromatic[(keyind+11)%12],chromatic[(keyind+1)%12]]

try:
	harp=imread("harp.png")
	plt.imshow(harp,cmap = cm.Greys_r)
	ax=plt.gca()

	bottom=[245,495,625,755,885,1015,1150,1280,1410,1540,1665]
	bottom.reverse()
	top=[245,495,625,755,885,1015,1150,1280,1410,1540,1665]
	top.reverse()
	y_bottom=510
	y_top=100

	if blow_bottom:
		plt.text(bottom.pop(),y_bottom,"Blow")
		plt.text(top.pop(),y_top,"Draw")
		plt.text(bottom.pop(),y_bottom,scale[0],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[1],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[2],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[4],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[4],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[6],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[0],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[1],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[2],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[3],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[4],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[5],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[0],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[6],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[2],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[1],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[4],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[3],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[0],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[5],horizontalalignment='center')
	else:
		plt.text(top.pop(),y_top,"Blow")
		plt.text(bottom.pop(),y_bottom,"Draw")
		plt.text(top.pop(),y_top,scale[0],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[1],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[2],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[4],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[4],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[6],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[0],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[1],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[2],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[3],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[4],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[5],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[0],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[6],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[2],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[1],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[4],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[3],horizontalalignment='center')
		plt.text(top.pop(),y_top,scale[0],horizontalalignment='center')
		plt.text(bottom.pop(),y_bottom,scale[5],horizontalalignment='center')
		
	plt.tick_params(which='both',bottom='off',top='off',left='off',right='off',labelbottom='off',labelleft='off')
	plt.show()
except IOError: 
	print "Harmonica image not found"
	pass
