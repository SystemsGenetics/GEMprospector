import itertools
import param
import upsetplot
import functools
import pandas as pd
import numpy as np

from ..abstract_plot_models import InterfacePlottingBase


class UpsetPlotInterface(InterfacePlottingBase):
    """
    Provides access to set overlap plots using UpsetPlot.

    This is needed as passing gene membership dictionaries to UpsetPlot
    does not always provide the correct counts."""

    show_counts = param.Boolean(default=True)

    @staticmethod
    def build_membership_series(gene_dict, min_size: int = 1):
        # dd = gene_dict.as_dict()
        keys = list(sorted(gene_dict.keys()))

        output = dict()

        for combo_len in range(2, len(keys) + 1):
            for key_combo in itertools.combinations(keys, combo_len):
                genes = [gene_dict[k] for k in key_combo]
                intersection_size = len(functools.reduce(np.intersect1d, genes))
                if intersection_size > min_size:
                    key = tuple(True if k in key_combo else False for k in keys)
                    output[key] = intersection_size

        idf = pd.DataFrame(output.keys(), columns=keys)
        index = pd.MultiIndex.from_frame(idf)
        return pd.Series(data=np.fromiter(output.values(), int), index=index)

    def __call__(self, *args, **kwargs):
        upset_series = self.build_membership_series(self.gene_set_collection.as_dict())
        return upsetplot.UpSet(upset_series, show_counts=self.show_counts)
