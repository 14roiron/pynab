#!/usr/bin/env bash

if [ "$1" == "CONNECTED" ]; then
	sudo systemctl restart nabairqualityd
	sudo systemctl restart nabweatherd
	echo '{"type":"command","sequence":[{"choreography":"nabtaichid/taichi.chor"}]}' | nc -4 -w 5 -v localhost 10543
fi

if [ "$1" == "HOTSPOT" ]; then
	echo '{"type":"command","sequence":[{"choreography":"nabd/rfid.chor"}]}' | nc -4 -w 5 -v localhost 10543
fi