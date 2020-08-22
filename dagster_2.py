from dagster import execute_pipeline , pipeline,solid

@solid
def get_number(_):
 return [1,3]


@solid
def get_sum(context,a):
    context.log.info("Result is : "+str(sum(a)))
@pipeline
def run_pipeline():
    get_sum(get_number())

if __name__=="__main__":
    execute_pipeline(run_pipeline)