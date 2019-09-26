<?php

use yii\db\Migration;

/**
 * Class m190926_090733_update_subject_table2
 */
class m190926_090733_update_subject_table2 extends Migration
{
    /**
     * {@inheritdoc}
     */
    public function safeUp()
    {
        $this->dropColumn('subject', 'update_at');
        $this->dropColumn('subject', 'update_by');

        $this->addColumn('subject', 'updated_at', $this->integer());
        $this->addColumn('subject', 'updated_by', $this->integer());
    }

    /**
     * {@inheritdoc}
     */
    public function safeDown()
    {
        echo "m190926_090733_update_subject_table2 cannot be reverted.\n";

        return false;
    }

    /*
    // Use up()/down() to run migration code without a transaction.
    public function up()
    {

    }

    public function down()
    {
        echo "m190926_090733_update_subject_table2 cannot be reverted.\n";

        return false;
    }
    */
}
