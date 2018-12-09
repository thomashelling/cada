# CADA
Community-aware detection of anomalies [1]

This is the code for detecting node anomalies in networks with NetworkX by including community structure from two out-of-the-box community detection algorithm: (1) Louvain [1], and (2) Infomap [2]. The algorithm is described <a href="https://link.springer.com/chapter/10.1007/978-3-030-05411-3_20">here</a>. 

For (1), Python package <a href="https://github.com/taynaud/python-louvain">Python-Louvain</a> is used. 

For (2), Python package <a href="https://pypi.org/project/infomap/">Infomap</a> is used.

[1] Helling, T.J., Scholtes, J. C., Takes, F.W. A community-aware approach for identifying node anomalies in complex networks. In Proceedings of the 7th International Conference on Complex Networks, CI, pages 244–255. Springer, 2019.

[2] Blondel, V.D., Guillaume, J.L., Lambiotte, R., Lefebvre, E.: Fast unfolding of communities in large networks. Journal of Statistical Mechanics: Theory and Experiment10008(10), 6 (2008)

[3] Rosvall, M., Bergstrom, C.: Maps of random walks on complex networks reveal community structure. Proceedings of National Academy of Sciences,105(4), 1118–1123 (2008)
