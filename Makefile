RESULTS:=$(patsubst %.py,%.result,$(wildcard *.py))

all: ${RESULTS}
%.result: %.py
	./$< > $@

.PHONY: clean
clean:
	rm -f *.result
