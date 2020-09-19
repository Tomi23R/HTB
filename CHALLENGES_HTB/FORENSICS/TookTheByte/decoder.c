#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	FILE* pf;
	int i;
	char* buffer;
	long filelen;
	FILE* escritura;
	char caracter;
	char clave = 0xFF;

	pf = fopen("password", "rb");
	escritura = fopen("decode_password","w");
		
	if(!pf){
		printf("Error abriendo el fichero");
		return -1;
	}

	fseek(pf, 0, SEEK_END);
	filelen = ftell(pf);
	rewind(pf);
	buffer = (char *)malloc((filelen + 1) * sizeof(char));

	for(i = 0; i < filelen; i++){
		fread(buffer + i, 1, 1, pf);
		caracter = clave ^ buffer[i];
		fwrite(&caracter, 1, 1, escritura);
	}

	fclose(pf);
	fclose(escritura);
	free(buffer);

	return 0;
}
