default: clean
	gcc dt.c -o dt
	./dt
clean:
	rm -f dt
