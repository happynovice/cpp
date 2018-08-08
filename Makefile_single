
file=197
#$(file):$(file).o
#       g++ -o  $(file) $(file).o
#$(file).o:$(file).cpp
#       g++ -c -std=c++11 $(file).cpp


$(file):$(file).o
        g++ -o $(file) $(file).o
$(file).o:$(file).cpp
        g++ -c -std=c++11 $(file).cpp 
clean:
        echo "wildcard $(CURDIR)/*.o"
        
        echo "$(wildcard $(CURDIR)/*.o)"
ifeq ("$(wildcard $(CURDIR)/$(file).o)","")
        echo "file not exists"
else
        rm $(file).o
endif
