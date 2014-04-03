This program scans an ascii text file (And it probably works for unicode, though I suspect less efficiently) for ASCII representations of floats, replaces those with a place-holder, and extracts the float value to a binary representation in a separate file.

Then, you can run your favorite compression algorithm on these files.

It's just a proof of concept at this point, and it does show that we can have more efficient lossless compression of some giant scientific data sets.

I hacked this out in a couple of hours, it's undocumented and not very good.

TODO:
Potentially each float has a different format. Currently there is only support for 127 different formats. (%x.yf in a format string) The first 31 get a one-byte encoding, while the rest get a 2-byte encoding. Sorting the format table by frequency, or using Huffman coding and a binary format for the text-with-placeholders would certainly make this more efficient.

Currently the format table is in order of appearance. If the first 31 formats seen are used infrequently, storage will be inefficient.

1) Sort format table.

FORMAT:

Basically text is transformed as follows:

All ASCII control characters (binary value < binary value of ' ') are quoted with a leading NUL character.

Control character NUL is reserved to indicate the beginning of something quoted.
Control characters 1-31 indicate a place holder 0-30

NUL followed by a _non_ control character indicate place holders 32-127.
(TODO: I should have a way to chain this to be even longer?, or if not chain, a way to actually describe the format specially for specific floats?)

(TODO: Of course I should do some kind of cost-benefit analysis per-float, if it is something like just 1.0 it is not worth all this, 1.0000000000000000000000000000000000001 has so little entropy that it probably compresses just fine with existing algorithms, but 1.xxxxxxxxxxxxxxxxxxxxxxx where xxxx are high-entropy, this may be better.)

(TODO: Figure out which floats can be stored as single vs which need to be double for lossless compression.)

Goals by phase of implementation
===============================

- Phase 0 (proof of concept) : 
	Separate numerical data from ASCII formatting, store numerical data in a binary format.

- Phase 1a : 
	Find better compression algorithms specifically for the numerical data. (See the bibliography.)

- Phase 1 :
	More storage formats (singles and doubles). Store each value in the smallest storage neede for lossless compression. (Depends on the format and number of digits after the decimal.)
	
	Find a better/more efficient set of control sequences / place holders. (Currently common control characters, such as \t and \n are being converted to a two byte representation. That is probably not good.)

- Phase 2:
	Detect large-scale formatting. For example "The next N floats are all tab/comma/space/space-tab separated values with M values per line" could be stored in a small representation. Especially if that format gets used over and over, then it would be possible for each place it is used to become a single byte place-holder in the ASCII.
	Large-scale formatting should work in blocks/regions, so that multiple large-scale formats can be included in a single file.

BIBLIOGRAPHY
===========
These papers describe algorithms for compressing floating point data arrays. They should give a much better compression ratio than various kinds of ZIP.


- http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.91.7936&rep=rep1&type=pdf
- http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.124.8968&rep=rep1&type=pdf
- http://users.ices.utexas.edu/~burtscher/papers/dcc07a.pdf
- http://users.ices.utexas.edu/~burtscher/papers/tr08.pdf
- http://www.ece.neu.edu/groups/nucar/GPGPU4/files/oneil.pdf
- http://www.cs.unc.edu/~isenburg/lcpfpv/
- https://xiph.org/flac/
- http://www.mcs.anl.gov/papers/P5009-0813_1.pdf
- http://users.ices.utexas.edu/~burtscher/papers/dcc06.pdf

