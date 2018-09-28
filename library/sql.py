#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

try:
  import sqlalchemy
except ImportError:
  sqlalchemy = None


def run_module():
  module_args = dict(
    connection=dict(type='str', required=True),
    query=dict(type='str', required=True),
    test_query=dict(type='str', required=False),
    test_result=dict(type='str', required=False, default=0)
  )
  module = AnsibleModule(
    argument_spec=module_args,
    supports_check_mode=True
  )
  result = dict(
    changed=False,
    original_message='',
    data=None,
    message=''
  )

  if sqlalchemy is None:
    module.fail_json(msg='sqlalchemy module is missing')

  engine = sqlalchemy.create_engine(module.params['connection'])

  if module.params['test_query']:
    try:
      res = engine.execute(module.params['test_query'])
    except sqlalchemy.exc.SQLAlchemyError as err:
      module.fail_json(msg="Error occurred running the test query: %s" % err)
      
    if str(res.scalar()) != module.params['test_result']:
      result['changed'] = True
  else:
    result['changed'] = True
    
  if module.check_mode:
    return result
  
  if result['changed'] == True:
    try:
      res = engine.execute(module.params['query'])
    except sqlalchemy.exc.SQLAlchemyError as err:
      module.fail_json(msg="Error occurred running the query: %s" % err)
      
    if res.returns_rows:
      result['data'] = res.fetchall()

  module.exit_json(**result)

def main():
  run_module()

if __name__ == '__main__':
    main()