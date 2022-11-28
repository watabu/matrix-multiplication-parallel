
CC = g++
FLAGS = -fopenmp

TARGET_SRCS = $(wildcard main_*.cpp) $(wildcard make_matrix_*.cpp)
TARGET_OBJS = $(patsubst %.cpp,%.o,$(TARGET_SRCS))
TARGET = $(patsubst %.cpp,%.out,$(TARGET_SRCS))

HEADER_SRCS = modules.cpp
HEADER_OBJS = $(patsubst %.cpp,%.o,$(HEADER_SRCS))

all: $(TARGET) $(TARGET_OBJS) $(HEADER_OBJS)

%.o: %.cpp $(HEADER_SRCS)
	$(CC) $(FLAGS) -c -o $@ $<

%.out: %.o $(HEADER_OBJS)
	$(CC) $(FLAGS) -o $@ $< $(HEADER_OBJS)

clean: 
	rm -f $(TARGET) $(TARGET_OBJS) $(HEADER_OBJS)

