# python-cli-pants-pandas-count-unique-name

## Description
A POC using pandas. Counts first field
deliminator by `-`.

## Tech stack
- pants
- python
  - pandas
  - pprint

## Docker stack
- pantsbuild/centos7:latest

## Notes
Use this to build the data file.
ls -Rlast | awk '
/:$/&&f{s=$0;f=0}
/:$/&&!f{sub(/:$/,"");s=$0;f=1;next}
NF&&f{ print s"/"$0 }' | awk '{ if (NF > 3 && $NF !~/^\./) print $0};' |  awk ' { printf "%s,%s,%s,%s,%s,%s,%s:%s;;%s;;%s,%s\n",$1,$2,$3,$4,$6,$5,$6,$7,$8,$9,$10,$11; } '

## To run
`sudo ./install.sh -u`

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`
