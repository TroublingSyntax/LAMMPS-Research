#!/usr/bin/env bash

for i in 1 2 3 4 5
do
  export PARSE_COUNT=$i
  sed -i.bak -r 's/input_from_shell/'$i'/' in.efield_modified
  mpirun -np 4 lmp_mpi < in.efield_modified
  python3 -c 'from dump_parse import dump_parser; dump_parser()'
  cp -f in.efield_modified.bak in.efield_modified
done

rm -r in.efield_modified.bak