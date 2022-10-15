import yaml

class GeneratorYml(object):

    def generateJobYml(self, job_object):
        path_to_file = 'generate_yml_k8s/templates/job.yml'
        with open(path_to_file) as f:
            template = f.read()

        template_final = template.format(
            env = yaml.dump(job_object)
        )
        
        return template_final
