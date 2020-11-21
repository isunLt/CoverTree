#include"cover_tree.h"

#include<pybind11/pybind11.h>
#include<pybind11/eigen.h>
#include<pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(covertreec, m){
    py::class_<CoverTree>(m, "CoverTree")
        .def(py::init([](matrixType& pMatrix, int truncate=-1, bool use_multi_core=true){
            return CoverTree::from_matrix(pMatrix, truncate, use_multi_core);
        }), py::arg("pMatrix"), py::arg("truncate")=-1, py::arg("use_multi_core")=true)
        .def("check_covering", &CoverTree::check_covering)
        .def("get_level_points", &CoverTree::get_level_points)
        .def("cal_level2ptsidx_pts2child", &CoverTree::cal_level2ptsidx_pts2child)
        .def("ret_level2ptsidx", &CoverTree::ret_level2ptsidx)
        .def("ret_pts2child", &CoverTree::ret_pts2child);
}