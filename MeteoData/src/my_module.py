'''
Created on Dec 29, 2017

@author: arturnowicki
'''
import luigi
import datetime

class ExtractData(luigi.Task):

    date = luigi.DateParameter(default = datetime.date.today())

    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget(self.date.strftime('../resources/icm_data.txt'))

    def run(self):
        with(self.output().open('w')) as output:
            output.write('example_data')
    
       

if __name__ == "__main__":
    luigi.run()
    