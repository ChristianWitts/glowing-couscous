startDay:
	mkdir -p $$DAY
	curl --cookie $$COOKIE -sS -o $$DAY/input "https://adventofcode.com/"$$YEAR"/day/"$$DAY"/input"
	cp starter.nim $$DAY/$$DAY".nim"

runDay:
	cd $$DAY; \
	nim c -r -d:release "day"$$DAY".nim"; \
	cd -
