import pandas as pd
import luigi
from random import randint


class AggregateMovieRatingTask(luigi.Task):
    years = luigi.ListParameter()

    def requires(self):
        return [GetMovieMetaDataTask(year) for year in self.years]

    def output(self):
        return luigi.LocalTarget('results.csv'.format(), format=UTF8)

    def run(self):
        data_frames = []

        for _input in self.input():
            with _input.open('r') as raw_file:
                data_frames.append(pd.read_csv(raw_file))

        df = pd.concat(data_frames)
        df = df.sort_values(['rating', 'votes'], ascending=[False, False])

        with self.output().open('w') as f:
            df[['title', 'rating', 'votes']].to_csv(f)

class create_df(luigi.Task):
    year = luigi.Parameter()

    def get_movie_meta_data(self):
        df.loc[, 'sum'] = randint(1, 100)
        return

    def output(self):
        return luigi.LocalTarget('raw-{}.csv'.format(self.year), sep=',', index=False)

    def run(self):
        self.df = pd.DataFrame({'Month':range(1, 13, 1), 'month_name':['jan', 'feb', 'march', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']})
        self.df['year'] = self.year()
        # with self.output().open('w') as csv_file:
        #     df = pd.DataFrame(payload)
        df.to_csv(csv_file)

if __name__ == '__main__':
    luigi.run()

print('luigi')