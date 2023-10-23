#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    if (!PyList_Check(p)) {
        fprintf(stderr, "Object is not a list\n");
        return;
    }

    PyListObject *obj = (PyListObject *)p;
    long int size = PyList_Size(p);

    if (size < 0) {
        fprintf(stderr, "Failed to get list size\n");
        return;
    }

    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", obj->allocated);

    for (long int i = 0; i < size; i++) {
        PyObject *item = obj->ob_item[i];
        printf("Element %li: %s\n", i, item->ob_type->tp_name);
    }
}
