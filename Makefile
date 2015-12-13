RESULTS:=$(patsubst %.py,%.result,$(wildcard *.py))

all: ${RESULTS}
%.result: %.py %.txt
	./$< > $@

.PHONY: clean
clean:
	rm -f *.result
