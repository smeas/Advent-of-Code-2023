#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

#define DIGIT_COUNT 9
char* DIGIT_NAMES[] = {
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
};

int parse_value(const char* str, int length)
{
	int digits[16];
	memset(digits, 0, sizeof(int) * 16);
	int digitIndex = 0;

	for (int i = 0; i < length; i++)
	{
		if (str[i] >= 49 && str[i] <= 57)
		{
			int digitValue = str[i] - 48;
			digits[digitIndex] = digitValue;
			digitIndex++;
		}
		else
		{
			for (int nameIndex = 0; nameIndex < DIGIT_COUNT; nameIndex++)
			{
				if (strncmp(&str[i], DIGIT_NAMES[nameIndex], strlen(DIGIT_NAMES[nameIndex])) != 0)
					continue;

				int digitValue = nameIndex + 1;
				digits[digitIndex] = digitValue;
				digitIndex++;
			}
		}
	}

	return digits[0] * 10 + digits[digitIndex - 1];
}

int main(int argc, char* argv[])
{
	int bufferSize = 1 << 16;
	char* buffer = malloc(bufferSize);
	memset(buffer, 0, bufferSize);

	FILE* file = fopen("input.txt", "r");
	int readBytes = fread(buffer, 1, bufferSize, file);
	fclose(file);
	assert(readBytes > 0);

	int sum = 0;
	char* ptr = buffer;
	while (1)
	{
		char* lineBreak = strchr(ptr, '\n');
		int length = lineBreak != NULL ? lineBreak - ptr : readBytes - (ptr - buffer);
		sum += parse_value(ptr, length);

		if (lineBreak == NULL)
			break;

		ptr = lineBreak + 1;
		if (ptr - buffer >= readBytes)
			break;
	}

	free(buffer);
	printf("solution: %i\n", sum);
	return 0;
}
