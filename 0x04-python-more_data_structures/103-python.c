#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *bytes_data;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes_data = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes_data);

    printf("  first 10 bytes:");
    for (i = 0; i < size && i < 10; i++) {
        printf(" %02x", bytes_data[i] & 0xff);
    }
    printf("\n");
}

