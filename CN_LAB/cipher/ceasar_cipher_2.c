#include <stdio.h>
#include <string.h>

void encrypt(char txt[], int key)
{
    char ch;

    for (int i = 0; txt[i] != '\0'; i++)
    {
        ch = txt[i];

        if (ch >= 'A' && ch <= 'Z')
        {
            ch = ch + key;
            if (ch > 'Z')
                ch = ch - 26;
            txt[i] = ch;
        }
        else if (ch >= 'a' && ch <= 'z')
        {
            ch = ch + key;
            if (ch > 'z')
                ch = ch - 26;
            txt[i] = ch;
        }
    }
}

void decryption(char txt[], int key)
{
    char ch;

    for (int i = 0; txt[i] != '\0'; i++)
    {
        ch = txt[i];

        if (ch >= 'A' && ch <= 'Z')
        {
            ch = ch - key;
            if (ch < 'A')
                ch = ch + 26;
            txt[i] = ch;
        }
        else if (ch >= 'a' && ch <= 'z')
        {
            ch = ch - key;
            if (ch < 'a')
                ch = ch + 26;
            txt[i] = ch;
        }
    }
}

int main()
{
    char txt[200];
    int key = 3;

    printf("Enter a simple string: ");
    fgets(txt, sizeof(txt), stdin);

    encrypt(txt, key);
    printf("The encrypted data is: %s", txt);

    decryption(txt, key);
    printf("The decrypted data is: %s", txt);

    return 0;
}
