//  g++ data.cpp -o data -fpie -Wl,-z,relro,-z,now -fcf-protection=none
#include <stdio.h>

extern "C" char *gets(char *s);

class Data
{
    char data[0x10];
public:
    virtual void get() {gets(data);}
    virtual void put() {puts(data);}
};

int main()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    Data *data[4];
    for (int i=0; i<4; i++)
        data[i] = new Data();

    printf("main: %p\n", main);
    printf("data: %p\n", data);
    printf("data[0]: %p\n", data[0]);
    printf("printf: %p\n", printf);

    while (true)
    {
        printf("> ");
        char buf[0x10];
        fgets(buf, 0x10, stdin);
        int command, index;
        sscanf(buf, "%d %d\n", &command, &index);

        if (command<0 || 2<=command ||
            index<0 || 4<=index)
            break;

        if (command==0)
            data[index]->get();
        if (command==1)
            data[index]->put();
    }
}
