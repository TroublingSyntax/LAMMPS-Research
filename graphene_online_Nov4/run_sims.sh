#!/usr/bin/env bash

BASE_FIELD_STRENGTH=15

for i in 1 2 3 4 5
do
  export PARSE_COUNT=$i
  FIELD_STRENGTH=$(($BASE_FIELD_STRENGTH * $i))
  sed -i -r 's/field_strength/'$FIELD_STRENGTH'/' in.efield
  mpirun -np 4 lmp_mpi < in.efield
  python3 -c 'from dump_parse import dump_parser; dump_parser()'
done