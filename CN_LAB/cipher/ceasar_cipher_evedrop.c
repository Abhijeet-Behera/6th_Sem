#include <stdio.h>
#include <string.h>

/* Encrypt */
void encrypt(char txt[], int key)
{
    for (int i = 0; txt[i]; i++)
    {
        char ch = txt[i];
        if (ch >= 'A' && ch <= 'Z')
        {
            ch += key;
            if (ch > 'Z') ch -= 26;
            txt[i] = ch;
        }
        else if (ch >= 'a' && ch <= 'z')
        {
            ch += key;
            if (ch > 'z') ch -= 26;
            txt[i] = ch;
        }
    }
}

/* Decrypt */
void decryption(char txt[], int key)
{
    for (int i = 0; txt[i]; i++)
    {
        char ch = txt[i];
        if (ch >= 'A' && ch <= 'Z')
        {
            ch -= key;
            if (ch < 'A') ch += 26;
            txt[i] = ch;
        }
        else if (ch >= 'a' && ch <= 'z')
        {
            ch -= key;
            if (ch < 'a') ch += 26;
            txt[i] = ch;
        }
    }
}

int eavesdrop(char cipher[])
{
    char temp[200];

    // Small built-in word list (local to function)
    const char *common_words[] = {
        "the", "and", "this", "hello", "you", "queen"
    };
    int wordCount = 6;

    int bestKey = -1;
    int bestScore = -1;

    for (int key = 1; key <= 25; key++)
    {
        strcpy(temp, cipher);
        decryption(temp, key);

        // convert to lowercase (inside eavesdrop)
        for (int i = 0; temp[i] != '\0'; i++)
        {
            if (temp[i] >= 'A' && temp[i] <= 'Z')
                temp[i] += 32;
        }

        int score = 0;

        // check for meaningful words
        for (int w = 0; w < wordCount; w++)
        {
            if (strstr(temp, common_words[w]) != NULL)
                score += 10;
        }

        // extra score for valid alphabetic text
        for (int i = 0; temp[i] != '\0'; i++)
        {
            if ((temp[i] >= 'a' && temp[i] <= 'z') || temp[i] == ' ')
                score++;
        }

        // choose best key
        if (score > bestScore)
        {
            bestScore = score;
            bestKey = key;
        }
    }

    return bestKey;
}





/* Main */
int main()
{
    char txt[200];
    int key = 4;

    printf("Enter a simple string: ");
    fgets(txt, sizeof(txt), stdin);

    encrypt(txt, key);
    printf("\nEncrypted text: %s", txt);

    int foundKey = eavesdrop(txt);

    printf("Recovered key: %d\n", foundKey);
    decryption(txt, foundKey);
    printf("Decrypted by attacker: %s", txt);

    return 0;
}
