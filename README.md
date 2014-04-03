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


