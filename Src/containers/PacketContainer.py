import pandas as pd
"""
 Class PacketContainer holds some data frame df.
"""


class PacketContainer(object):

    def __init__(self, df):
        self.df = df

    """
        function return the df frame the PacketContainer class holds 
    """
    def get_df(self):
        return self.df



