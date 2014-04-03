#!/usr/bin/env python
from itertools import *
import re

SPACE_CHAR = ' '
SPACE_ASCII = ord(SPACE_CHAR)
NULL_ASCII = 0
NULL_CHAR = chr(0)

def is_control(character):
	return ord(character) < SPACE_ASCII

def escape_int(inint):
	as_char = chr(inint + 1)
	if not is_control(as_char):
		return NULL_CHAR + as_char
	else:
		return as_char

def quote_ascii(instring):
	ret = ""
	for one_char in instring:
		if ord(one_char) < SPACE_ASCII:
			ret += chr(0) + one_char
		else:
			ret += one_char
	return ret

def unquote_ascii(instring):
	instring = list(instring)
	retstring = ""


	while len(instring) > 0:
		current_char = instring.pop(0)

		if not is_control(current_char):
			retstring += current_char
			continue
		else: # a control characte
			numerical_value = 0
			if ord(current_char) == NULL_ASCII:
				escaped_value = instring.pop(0)
				if is_control(escaped_value):
					retstring += escaped_value
					continue
				else:
					numerical_value = ord(escaped_value)
			else:#some other control character
				numerical_value = ord(current_char)
			assert numerical_value != 0, "Should not happen"
			numerical_value -= 1
			yield retstring
			retstring = ""
			yield numerical_value
			#continue
	if retstring is not "":
		yield retstring

simple_float = re.compile("\d+\.\d+")
def find_floats(string):
	non_floats = simple_float.split(string)
	floats = simple_float.findall(string)

	return non_floats, floats

def find_and_format(string):
	sub_strs, floats = find_floats(string)

	formats = [(tuple(map(len, f.split('.'))), f) for f in floats]

	format_set = set([i for i,j in formats])


	format_hash = dict(zip(format_set, count(0)))
	format_table = dict([(i,j) for j,i in format_hash.iteritems()])

	formats = [format_hash.get(i) for i,j in formats]
	floats = map(float, floats)

	#now we have: sub_strs, formats, floats, and format_table
	return sub_strs, formats, floats, format_table

def quote_split(some_text):
	sub_strs, formats, floats, format_table = find_and_format(some_text)

	sub_strs = map(quote_ascii, sub_strs)
	
	text = ""
	for plain, format in izip(sub_strs[:-1], formats):
		text += plain + escape_int(format)
	text += sub_strs[-1]

	return text, floats, format_table

class formatter(object):
	def __init__(self, a,b):
		self.fmtstr = "%" + str(a) + "." + str(b) + "f"

	def __call__(self, float):
		return self.fmtstr%float

def format_table_to_format_functions(format_table):
	retdict = dict()

	for k, v in format_table.iteritems():
		retdict[k] = formatter(v[0],v[1])
	return retdict

def quote_combine(text, floats, format_table):
	
	format_funcs = format_table_to_format_functions(format_table)
	
	out_text = ""
	tokens = unquote_ascii(text)
	for t in tokens:
		if type(t) in [str]:
			out_text += t
			continue
		#must be an int (or other control code if we extend this)
		out_text += format_funcs[t](floats.pop(0))
	
	return out_text
	


if __name__ == "__main__":
	mystr = "this is a test " + chr(0) + " foobarbaz"
	quoted =  quote_ascii(mystr)
	print repr(quoted)
	rebuilt = "".join([i for i in unquote_ascii(quoted)])
	print "mystr == rebuilt : " , mystr == rebuilt

	all_control = ' '.join(map(chr,range(128)))
	all_quoted = quote_ascii(all_control)
	print repr(all_quoted)
	all_rebuilt = ''.join([i for i in unquote_ascii(all_quoted)])
	print "all_control == all_rebuilt : ", all_control == all_rebuilt

	test_mixed = """
	uni:0.296203966948793):0.0198614304913658):0.00313131156568666,(Ochrogaster_lunifer:0.0335397657256079,Leucoptera_malifoliella:0.182398130282726):0.204654940030161):0.0285165061041942):0.09061
	25666360033,Anopheles_janconnae:0.0296054179988425):0.23297075510678,Psacothea_hilaris:0.116613155785488):0.14300025246744,Libelloides_macaronius:0.126125873732874):0.113157561360003,((((((Cul
	ex_quinquefasciatus:0.128071805904412,Hydaropsis_longirostris:0.232767699087299):0.0756506729636065,Papilio_maraho:0.132131329339393):0.0693022898276685,((Drosophila_littoralis:0.0675965217657
	067,(Fergusonina_sp:0.0118042970178113,Fergusonina_taylori:0.0273468886324472):0.13320494600693):0.183729959583521,(Radoszkowskius_oculata:0.483929844509303,Chauliognathus_opacus:0.13049475006
	1746):0.0144023962254054):0.169225394395885):1.60198243883956e-05,Calosoma_sp:0.225135731050968):0.0318179868523602,Saturnia_boisduvalii:0.171394047556305):0.019931413637447,Pieris_rapae:0.177565426475903):0.035014799384982):0.00768938639746985,Ctenoptilum_vasava:0.224094258552591):0.0366767838042755):0.224978718946498,Pristomyrmex_punctatus:0.179458026630544,Cephus_cinctus:0.473643725204688);
	1
	8.32447056025
	0.612247538276
	5000
	9.75683378985
	0.785629412398  0.451207130083  0.578293117491  1.15091849484   

	0.802012262232  0.825449905706  0.709524362196  1.60867293101   1.57365779191   0.470584293816  

	0.50410073019   0.0112524472997 0.0210404324894 0.463606390021  
	0.048633128877  0.0768247243058 0.00958532684383        0.864956819973  
	0.162594297468  0.070392991515  0.0245891591225 0.742423551894  
	0.441329986715  0.00980131982253        0.102325662397  0.446543031065  
	0.0292357753269 0.179832097862  0.0210820261087 0.769850100702  
	0.0267404315607 0.908333737631  0.0180542065187 0.0468716242896 
	0.0861348350274 0.00622694813271        0.289835799751  0.617802417089  
	0.602019418358  0.0104031257314 0.225365910904  0.162211545006  
	0.717769999178  0.00520863106162        0.249239274839  0.0277820949206 
	0.017409301224  0.175557368003  0.780909985125  0.0261233456481 
	0.743394195269  0.0273672613383 0.0205452644774 0.208693278916  
	0.0584151337798 0.097362698597  0.270780012832  0.573442154791  
	0.707523442908  0.00769127647777        0.0730814093904 0.211703871224  
	0.157782880864  0.322778872355  0.285144353627  0.234293893154  
	0.0370108519042 0.0954211619303 0.660541958011  0.207026028155  
	0.652377049752  0.0770410996937 0.0751890240406 0.195392826513  
	0.214985030293  0.00614055801601        0.615024755845  0.163849655846  
	0.225389618052  0.0148086743634 0.0394970620291 0.720304645556  
	0.79514168245   0.0714877318432 0.0399749404705 0.0933956452367 
	0.53034370836   0.0365042684262 0.348832010177  0.0843200130362 
	0.797499469215  0.0120892949631 0.104685381278  0.0857258545441 
	0.536911204749  0.0474624759152 0.0331488201886 0.382477499147  
	0.330074593462  0.0455863791227 0.0231825223289 0.601156505086  
	0.0634716703549 0.0576030497373 0.131509675441  0.747415604466  
	0.340976382049  0.175331986371  0.0417037900684 0.441987841511  
	0.349323615727  0.00336967888599        0.606040463369  0.0412662420189 
	0.325893300113  0.0692610791681 0.119787923369  0.48505769735   
	0.0128323060265 0.0990355031096 0.00458172762244        0.883550463241  
	0.237401923487  0.0216131905593 0.295548225404  0.44543666055   
	0.0996363577612 0.0340124121964 0.392446779402  0.47390445064   
	"""

	print quote_split(test_mixed)
