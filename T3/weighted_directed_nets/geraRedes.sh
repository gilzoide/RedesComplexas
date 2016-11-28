#!/bin/sh

for dec in $(seq 0 5); do
	./benchmark -N 128 -k 16 -maxk 16 -muw 0.1 -minc 32 -maxc 32 -beta 1.$dec
	mkdir -p rede$dec
	mv network.dat statistics.dat community.dat rede$dec
done
