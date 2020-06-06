#include <Python.h>

static PyObject* helloworld(PyObject* self)
{
int a=3 ,b=4,sum=0;
sum = a+b;
printf("sum is %d\n",sum);
	return Py_BuildValue("s" , "Hello , Python extension!!\n");
}
 
//static char helloworld_docs[] =
//"helloworld(): Any message you want to put here""\n";

static PyMethodDef helloworld_func[] = {
{ "helloworld" , (PyCFunction)helloworld, METH_NOARGS},{NULL}};

void inithelloworld(void)
{
	Py_InitModule3("helloworld" , helloworld_func,"Extension module example");
}


